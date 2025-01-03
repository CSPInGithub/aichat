FFmpeg 64-bit static Windows build from www.gyan.dev

Version: 2025-01-02-git-0457aaf0d3-full_build-www.gyan.dev

License: GPL v3

Source Code: https://github.com/FFmpeg/FFmpeg/commit/0457aaf0d3

External Assets
frei0r plugins:   https://www.gyan.dev/ffmpeg/builds/ffmpeg-frei0r-plugins
lensfun database: https://www.gyan.dev/ffmpeg/builds/ffmpeg-lensfun-db

git-full build configuration: 

ARCH                      x86 (generic)
big-endian                no
runtime cpu detection     yes
standalone assembly       yes
x86 assembler             nasm
MMX enabled               yes
MMXEXT enabled            yes
3DNow! enabled            yes
3DNow! extended enabled   yes
SSE enabled               yes
SSSE3 enabled             yes
AESNI enabled             yes
AVX enabled               yes
AVX2 enabled              yes
AVX-512 enabled           yes
AVX-512ICL enabled        yes
XOP enabled               yes
FMA3 enabled              yes
FMA4 enabled              yes
i686 features enabled     yes
CMOV is fast              yes
EBX available             yes
EBP available             yes
debug symbols             yes
strip symbols             yes
optimize for size         no
optimizations             yes
static                    yes
shared                    no
postprocessing support    yes
network support           yes
threading support         pthreads
safe bitstream reader     yes
texi2html enabled         no
perl enabled              yes
pod2man enabled           yes
makeinfo enabled          yes
makeinfo supports HTML    yes
xmllint enabled           yes

External libraries:
avisynth                libharfbuzz             libsvtav1
bzlib                   libilbc                 libtheora
chromaprint             libjxl                  libtwolame
frei0r                  liblc3                  libuavs3d
gmp                     liblensfun              libvidstab
gnutls                  libmodplug              libvmaf
iconv                   libmp3lame              libvo_amrwbenc
ladspa                  libmysofa               libvorbis
lcms2                   libopencore_amrnb       libvpx
libaom                  libopencore_amrwb       libvvenc
libaribb24              libopenjpeg             libwebp
libaribcaption          libopenmpt              libx264
libass                  libopus                 libx265
libbluray               libplacebo              libxavs2
libbs2b                 libqrencode             libxevd
libcaca                 libquirc                libxeve
libcdio                 librav1e                libxml2
libcodec2               librist                 libxvid
libdav1d                librubberband           libzimg
libdavs2                libshaderc              libzmq
libflite                libshine                libzvbi
libfontconfig           libsnappy               lzma
libfreetype             libsoxr                 mediafoundation
libfribidi              libspeex                sdl2
libgme                  libsrt                  zlib
libgsm                  libssh

External libraries providing hardware acceleration:
amf                     d3d12va                 nvdec
cuda                    dxva2                   nvenc
cuda_llvm               ffnvcodec               opencl
cuvid                   libmfx                  vaapi
d3d11va                 libvpl                  vulkan

Libraries:
avcodec                 avformat                swresample
avdevice                avutil                  swscale
avfilter                postproc

Programs:
ffmpeg                  ffplay                  ffprobe

Enabled decoders:
aac                     g723_1                  pdv
aac_fixed               g729                    pfm
aac_latm                gdv                     pgm
aasc                    gem                     pgmyuv
ac3                     gif                     pgssub
ac3_fixed               gremlin_dpcm            pgx
acelp_kelvin            gsm                     phm
adpcm_4xm               gsm_ms                  photocd
adpcm_adx               h261                    pictor
adpcm_afc               h263                    pixlet
adpcm_agm               h263i                   pjs
adpcm_aica              h263p                   png
adpcm_argo              h264                    ppm
adpcm_ct                h264_cuvid              prores
adpcm_dtk               h264_qsv                prosumer
adpcm_ea                hap                     psd
adpcm_ea_maxis_xa       hca                     ptx
adpcm_ea_r1             hcom                    qcelp
adpcm_ea_r2             hdr                     qdm2
adpcm_ea_r3             hevc                    qdmc
adpcm_ea_xas            hevc_cuvid              qdraw
adpcm_g722              hevc_qsv                qoa
adpcm_g726              hnm4_video              qoi
adpcm_g726le            hq_hqa                  qpeg
adpcm_ima_acorn         hqx                     qtrle
adpcm_ima_alp           huffyuv                 r10k
adpcm_ima_amv           hymt                    r210
adpcm_ima_apc           iac                     ra_144
adpcm_ima_apm           idcin                   ra_288
adpcm_ima_cunning       idf                     ralf
adpcm_ima_dat4          iff_ilbm                rasc
adpcm_ima_dk3           ilbc                    rawvideo
adpcm_ima_dk4           imc                     realtext
adpcm_ima_ea_eacs       imm4                    rka
adpcm_ima_ea_sead       imm5                    rl2
adpcm_ima_iss           indeo2                  roq
adpcm_ima_moflex        indeo3                  roq_dpcm
adpcm_ima_mtf           indeo4                  rpza
adpcm_ima_oki           indeo5                  rscc
adpcm_ima_qt            interplay_acm           rtv1
adpcm_ima_rad           interplay_dpcm          rv10
adpcm_ima_smjpeg        interplay_video         rv20
adpcm_ima_ssi           ipu                     rv30
adpcm_ima_wav           jacosub                 rv40
adpcm_ima_ws            jpeg2000                rv60
adpcm_ima_xbox          jpegls                  s302m
adpcm_ms                jv                      sami
adpcm_mtaf              kgv1                    sanm
adpcm_psx               kmvc                    sbc
adpcm_sbpro_2           lagarith                scpr
adpcm_sbpro_3           lead                    screenpresso
adpcm_sbpro_4           libaom_av1              sdx2_dpcm
adpcm_swf               libaribb24              sga
adpcm_thp               libaribcaption          sgi
adpcm_thp_le            libcodec2               sgirle
adpcm_vima              libdav1d                sheervideo
adpcm_xa                libdavs2                shorten
adpcm_xmd               libgsm                  simbiosis_imx
adpcm_yamaha            libgsm_ms               sipr
adpcm_zork              libilbc                 siren
agm                     libjxl                  smackaud
aic                     liblc3                  smacker
alac                    libopencore_amrnb       smc
alias_pix               libopencore_amrwb       smvjpeg
als                     libopus                 snow
amrnb                   libspeex                sol_dpcm
amrwb                   libuavs3d               sonic
amv                     libvorbis               sp5x
anm                     libvpx_vp8              speedhq
ansi                    libvpx_vp9              speex
anull                   libxevd                 srgc
apac                    libzvbi_teletext        srt
ape                     loco                    ssa
apng                    lscr                    stl
aptx                    m101                    subrip
aptx_hd                 mace3                   subviewer
arbc                    mace6                   subviewer1
argo                    magicyuv                sunrast
ass                     mdec                    svq1
asv1                    media100                svq3
asv2                    metasound               tak
atrac1                  microdvd                targa
atrac3                  mimic                   targa_y216
atrac3al                misc4                   tdsc
atrac3p                 mjpeg                   text
atrac3pal               mjpeg_cuvid             theora
atrac9                  mjpeg_qsv               thp
aura                    mjpegb                  tiertexseqvideo
aura2                   mlp                     tiff
av1                     mmvideo                 tmv
av1_cuvid               mobiclip                truehd
av1_qsv                 motionpixels            truemotion1
avrn                    movtext                 truemotion2
avrp                    mp1                     truemotion2rt
avs                     mp1float                truespeech
avui                    mp2                     tscc
bethsoftvid             mp2float                tscc2
bfi                     mp3                     tta
bink                    mp3adu                  twinvq
binkaudio_dct           mp3adufloat             txd
binkaudio_rdft          mp3float                ulti
bintext                 mp3on4                  utvideo
bitpacked               mp3on4float             v210
bmp                     mpc7                    v210x
bmv_audio               mpc8                    v308
bmv_video               mpeg1_cuvid             v408
bonk                    mpeg1video              v410
brender_pix             mpeg2_cuvid             vb
c93                     mpeg2_qsv               vble
cavs                    mpeg2video              vbn
cbd2_dpcm               mpeg4                   vc1
ccaption                mpeg4_cuvid             vc1_cuvid
cdgraphics              mpegvideo               vc1_qsv
cdtoons                 mpl2                    vc1image
cdxl                    msa1                    vcr1
cfhd                    mscc                    vmdaudio
cinepak                 msmpeg4v1               vmdvideo
clearvideo              msmpeg4v2               vmix
cljr                    msmpeg4v3               vmnc
cllc                    msnsiren                vnull
comfortnoise            msp2                    vorbis
cook                    msrle                   vp3
cpia                    mss1                    vp4
cri                     mss2                    vp5
cscd                    msvideo1                vp6
cyuv                    mszh                    vp6a
dca                     mts2                    vp6f
dds                     mv30                    vp7
derf_dpcm               mvc1                    vp8
dfa                     mvc2                    vp8_cuvid
dfpwm                   mvdv                    vp8_qsv
dirac                   mvha                    vp9
dnxhd                   mwsc                    vp9_cuvid
dolby_e                 mxpeg                   vp9_qsv
dpx                     nellymoser              vplayer
dsd_lsbf                notchlc                 vqa
dsd_lsbf_planar         nuv                     vqc
dsd_msbf                on2avc                  vvc
dsd_msbf_planar         opus                    vvc_qsv
dsicinaudio             osq                     wady_dpcm
dsicinvideo             paf_audio               wavarc
dss_sp                  paf_video               wavpack
dst                     pam                     wbmp
dvaudio                 pbm                     wcmv
dvbsub                  pcm_alaw                webp
dvdsub                  pcm_bluray              webvtt
dvvideo                 pcm_dvd                 wmalossless
dxa                     pcm_f16le               wmapro
dxtory                  pcm_f24le               wmav1
dxv                     pcm_f32be               wmav2
eac3                    pcm_f32le               wmavoice
eacmv                   pcm_f64be               wmv1
eamad                   pcm_f64le               wmv2
eatgq                   pcm_lxf                 wmv3
eatgv                   pcm_mulaw               wmv3image
eatqi                   pcm_s16be               wnv1
eightbps                pcm_s16be_planar        wrapped_avframe
eightsvx_exp            pcm_s16le               ws_snd1
eightsvx_fib            pcm_s16le_planar        xan_dpcm
escape124               pcm_s24be               xan_wc3
escape130               pcm_s24daud             xan_wc4
evrc                    pcm_s24le               xbin
exr                     pcm_s24le_planar        xbm
fastaudio               pcm_s32be               xface
ffv1                    pcm_s32le               xl
ffvhuff                 pcm_s32le_planar        xma1
ffwavesynth             pcm_s64be               xma2
fic                     pcm_s64le               xpm
fits                    pcm_s8                  xsub
flac                    pcm_s8_planar           xwd
flashsv                 pcm_sga                 y41p
flashsv2                pcm_u16be               ylc
flic                    pcm_u16le               yop
flv                     pcm_u24be               yuv4
fmvc                    pcm_u24le               zero12v
fourxm                  pcm_u32be               zerocodec
fraps                   pcm_u32le               zlib
frwu                    pcm_u8                  zmbv
ftr                     pcm_vidc
g2m                     pcx

Enabled encoders:
a64multi                hevc_nvenc              pcm_s64be
a64multi5               hevc_qsv                pcm_s64le
aac                     hevc_vaapi              pcm_s8
aac_mf                  hevc_vulkan             pcm_s8_planar
ac3                     huffyuv                 pcm_u16be
ac3_fixed               jpeg2000                pcm_u16le
ac3_mf                  jpegls                  pcm_u24be
adpcm_adx               libaom_av1              pcm_u24le
adpcm_argo              libcodec2               pcm_u32be
adpcm_g722              libgsm                  pcm_u32le
adpcm_g726              libgsm_ms               pcm_u8
adpcm_g726le            libilbc                 pcm_vidc
adpcm_ima_alp           libjxl                  pcx
adpcm_ima_amv           liblc3                  pfm
adpcm_ima_apm           libmp3lame              pgm
adpcm_ima_qt            libopencore_amrnb       pgmyuv
adpcm_ima_ssi           libopenjpeg             phm
adpcm_ima_wav           libopus                 png
adpcm_ima_ws            librav1e                ppm
adpcm_ms                libshine                prores
adpcm_swf               libspeex                prores_aw
adpcm_yamaha            libsvtav1               prores_ks
alac                    libtheora               qoi
alias_pix               libtwolame              qtrle
amv                     libvo_amrwbenc          r10k
anull                   libvorbis               r210
apng                    libvpx_vp8              ra_144
aptx                    libvpx_vp9              rawvideo
aptx_hd                 libvvenc                roq
ass                     libwebp                 roq_dpcm
asv1                    libwebp_anim            rpza
asv2                    libx264                 rv10
av1_amf                 libx264rgb              rv20
av1_mf                  libx265                 s302m
av1_nvenc               libxavs2                sbc
av1_qsv                 libxeve                 sgi
av1_vaapi               libxvid                 smc
avrp                    ljpeg                   snow
avui                    magicyuv                speedhq
bitpacked               mjpeg                   srt
bmp                     mjpeg_qsv               ssa
cfhd                    mjpeg_vaapi             subrip
cinepak                 mlp                     sunrast
cljr                    movtext                 svq1
comfortnoise            mp2                     targa
dca                     mp2fixed                text
dfpwm                   mp3_mf                  tiff
dnxhd                   mpeg1video              truehd
dpx                     mpeg2_qsv               tta
dvbsub                  mpeg2_vaapi             ttml
dvdsub                  mpeg2video              utvideo
dvvideo                 mpeg4                   v210
dxv                     msmpeg4v2               v308
eac3                    msmpeg4v3               v408
exr                     msrle                   v410
ffv1                    msvideo1                vbn
ffv1_vulkan             nellymoser              vc2
ffvhuff                 opus                    vnull
fits                    pam                     vorbis
flac                    pbm                     vp8_vaapi
flashsv                 pcm_alaw                vp9_qsv
flashsv2                pcm_bluray              vp9_vaapi
flv                     pcm_dvd                 wavpack
g723_1                  pcm_f32be               wbmp
gif                     pcm_f32le               webvtt
h261                    pcm_f64be               wmav1
h263                    pcm_f64le               wmav2
h263p                   pcm_mulaw               wmv1
h264_amf                pcm_s16be               wmv2
h264_mf                 pcm_s16be_planar        wrapped_avframe
h264_nvenc              pcm_s16le               xbm
h264_qsv                pcm_s16le_planar        xface
h264_vaapi              pcm_s24be               xsub
h264_vulkan             pcm_s24daud             xwd
hap                     pcm_s24le               y41p
hdr                     pcm_s24le_planar        yuv4
hevc_amf                pcm_s32be               zlib
hevc_d3d12va            pcm_s32le               zmbv
hevc_mf                 pcm_s32le_planar

Enabled hwaccels:
av1_d3d11va             hevc_dxva2              vc1_dxva2
av1_d3d11va2            hevc_nvdec              vc1_nvdec
av1_d3d12va             hevc_vaapi              vc1_vaapi
av1_dxva2               hevc_vulkan             vp8_nvdec
av1_nvdec               mjpeg_nvdec             vp8_vaapi
av1_vaapi               mjpeg_vaapi             vp9_d3d11va
av1_vulkan              mpeg1_nvdec             vp9_d3d11va2
h263_vaapi              mpeg2_d3d11va           vp9_d3d12va
h264_d3d11va            mpeg2_d3d11va2          vp9_dxva2
h264_d3d11va2           mpeg2_d3d12va           vp9_nvdec
h264_d3d12va            mpeg2_dxva2             vp9_vaapi
h264_dxva2              mpeg2_nvdec             vvc_vaapi
h264_nvdec              mpeg2_vaapi             wmv3_d3d11va
h264_vaapi              mpeg4_nvdec             wmv3_d3d11va2
h264_vulkan             mpeg4_vaapi             wmv3_d3d12va
hevc_d3d11va            vc1_d3d11va             wmv3_dxva2
hevc_d3d11va2           vc1_d3d11va2            wmv3_nvdec
hevc_d3d12va            vc1_d3d12va             wmv3_vaapi

Enabled parsers:
aac                     dvdsub                  mpegvideo
aac_latm                evc                     opus
ac3                     flac                    png
adx                     ftr                     pnm
amr                     g723_1                  qoi
av1                     g729                    rv34
avs2                    gif                     sbc
avs3                    gsm                     sipr
bmp                     h261                    tak
cavsvideo               h263                    vc1
cook                    h264                    vorbis
cri                     hdr                     vp3
dca                     hevc                    vp8
dirac                   ipu                     vp9
dnxhd                   jpeg2000                vvc
dnxuc                   jpegxl                  webp
dolby_e                 misc4                   xbm
dpx                     mjpeg                   xma
dvaudio                 mlp                     xwd
dvbsub                  mpeg4video
dvd_nav                 mpegaudio

Enabled demuxers:
aa                      idf                     pcm_f64le
aac                     iff                     pcm_mulaw
aax                     ifv                     pcm_s16be
ac3                     ilbc                    pcm_s16le
ac4                     image2                  pcm_s24be
ace                     image2_alias_pix        pcm_s24le
acm                     image2_brender_pix      pcm_s32be
act                     image2pipe              pcm_s32le
adf                     image_bmp_pipe          pcm_s8
adp                     image_cri_pipe          pcm_u16be
ads                     image_dds_pipe          pcm_u16le
adx                     image_dpx_pipe          pcm_u24be
aea                     image_exr_pipe          pcm_u24le
afc                     image_gem_pipe          pcm_u32be
aiff                    image_gif_pipe          pcm_u32le
aix                     image_hdr_pipe          pcm_u8
alp                     image_j2k_pipe          pcm_vidc
amr                     image_jpeg_pipe         pdv
amrnb                   image_jpegls_pipe       pjs
amrwb                   image_jpegxl_pipe       pmp
anm                     image_pam_pipe          pp_bnk
apac                    image_pbm_pipe          pva
apc                     image_pcx_pipe          pvf
ape                     image_pfm_pipe          qcp
apm                     image_pgm_pipe          qoa
apng                    image_pgmyuv_pipe       r3d
aptx                    image_pgx_pipe          rawvideo
aptx_hd                 image_phm_pipe          rcwt
aqtitle                 image_photocd_pipe      realtext
argo_asf                image_pictor_pipe       redspark
argo_brp                image_png_pipe          rka
argo_cvg                image_ppm_pipe          rl2
asf                     image_psd_pipe          rm
asf_o                   image_qdraw_pipe        roq
ass                     image_qoi_pipe          rpl
ast                     image_sgi_pipe          rsd
au                      image_sunrast_pipe      rso
av1                     image_svg_pipe          rtp
avi                     image_tiff_pipe         rtsp
avisynth                image_vbn_pipe          s337m
avr                     image_webp_pipe         sami
avs                     image_xbm_pipe          sap
avs2                    image_xpm_pipe          sbc
avs3                    image_xwd_pipe          sbg
bethsoftvid             imf                     scc
bfi                     ingenient               scd
bfstm                   ipmovie                 sdns
bink                    ipu                     sdp
binka                   ircam                   sdr2
bintext                 iss                     sds
bit                     iv8                     sdx
bitpacked               ivf                     segafilm
bmv                     ivr                     ser
boa                     jacosub                 sga
bonk                    jpegxl_anim             shorten
brstm                   jv                      siff
c93                     kux                     simbiosis_imx
caf                     kvag                    sln
cavsvideo               laf                     smacker
cdg                     lc3                     smjpeg
cdxl                    libgme                  smush
cine                    libmodplug              sol
codec2                  libopenmpt              sox
codec2raw               live_flv                spdif
concat                  lmlm4                   srt
dash                    loas                    stl
data                    lrc                     str
daud                    luodat                  subviewer
dcstr                   lvf                     subviewer1
derf                    lxf                     sup
dfa                     m4v                     svag
dfpwm                   matroska                svs
dhav                    mca                     swf
dirac                   mcc                     tak
dnxhd                   mgsts                   tedcaptions
dsf                     microdvd                thp
dsicin                  mjpeg                   threedostr
dss                     mjpeg_2000              tiertexseq
dts                     mlp                     tmv
dtshd                   mlv                     truehd
dv                      mm                      tta
dvbsub                  mmf                     tty
dvbtxt                  mods                    txd
dxa                     moflex                  ty
ea                      mov                     usm
ea_cdata                mp3                     v210
eac3                    mpc                     v210x
epaf                    mpc8                    vag
evc                     mpegps                  vc1
ffmetadata              mpegts                  vc1t
filmstrip               mpegtsraw               vividas
fits                    mpegvideo               vivo
flac                    mpjpeg                  vmd
flic                    mpl2                    vobsub
flv                     mpsub                   voc
fourxm                  msf                     vpk
frm                     msnwc_tcp               vplayer
fsb                     msp                     vqf
fwse                    mtaf                    vvc
g722                    mtv                     w64
g723_1                  musx                    wady
g726                    mv                      wav
g726le                  mvi                     wavarc
g729                    mxf                     wc3
gdv                     mxg                     webm_dash_manifest
genh                    nc                      webvtt
gif                     nistsphere              wsaud
gsm                     nsp                     wsd
gxf                     nsv                     wsvqa
h261                    nut                     wtv
h263                    nuv                     wv
h264                    obu                     wve
hca                     ogg                     xa
hcom                    oma                     xbin
hevc                    osq                     xmd
hls                     paf                     xmv
hnm                     pcm_alaw                xvag
iamf                    pcm_f32be               xwma
ico                     pcm_f32le               yop
idcin                   pcm_f64be               yuv4mpegpipe

Enabled muxers:
a64                     h263                    pcm_s24be
ac3                     h264                    pcm_s24le
ac4                     hash                    pcm_s32be
adts                    hds                     pcm_s32le
adx                     hevc                    pcm_s8
aea                     hls                     pcm_u16be
aiff                    iamf                    pcm_u16le
alp                     ico                     pcm_u24be
amr                     ilbc                    pcm_u24le
amv                     image2                  pcm_u32be
apm                     image2pipe              pcm_u32le
apng                    ipod                    pcm_u8
aptx                    ircam                   pcm_vidc
aptx_hd                 ismv                    psp
argo_asf                ivf                     rawvideo
argo_cvg                jacosub                 rcwt
asf                     kvag                    rm
asf_stream              latm                    roq
ass                     lc3                     rso
ast                     lrc                     rtp
au                      m4v                     rtp_mpegts
avi                     matroska                rtsp
avif                    matroska_audio          sap
avm2                    md5                     sbc
avs2                    microdvd                scc
avs3                    mjpeg                   segafilm
bit                     mkvtimestamp_v2         segment
caf                     mlp                     smjpeg
cavsvideo               mmf                     smoothstreaming
chromaprint             mov                     sox
codec2                  mp2                     spdif
codec2raw               mp3                     spx
crc                     mp4                     srt
dash                    mpeg1system             stream_segment
data                    mpeg1vcd                streamhash
daud                    mpeg1video              sup
dfpwm                   mpeg2dvd                swf
dirac                   mpeg2svcd               tee
dnxhd                   mpeg2video              tg2
dts                     mpeg2vob                tgp
dv                      mpegts                  truehd
eac3                    mpjpeg                  tta
evc                     mxf                     ttml
f4v                     mxf_d10                 uncodedframecrc
ffmetadata              mxf_opatom              vc1
fifo                    null                    vc1t
filmstrip               nut                     voc
fits                    obu                     vvc
flac                    oga                     w64
flv                     ogg                     wav
framecrc                ogv                     webm
framehash               oma                     webm_chunk
framemd5                opus                    webm_dash_manifest
g722                    pcm_alaw                webp
g723_1                  pcm_f32be               webvtt
g726                    pcm_f32le               wsaud
g726le                  pcm_f64be               wtv
gif                     pcm_f64le               wv
gsm                     pcm_mulaw               yuv4mpegpipe
gxf                     pcm_s16be
h261                    pcm_s16le

Enabled protocols:
async                   http                    rtmp
bluray                  httpproxy               rtmpe
cache                   https                   rtmps
concat                  icecast                 rtmpt
concatf                 ipfs_gateway            rtmpte
crypto                  ipns_gateway            rtmpts
data                    librist                 rtp
fd                      libsrt                  srtp
ffrtmpcrypt             libssh                  subfile
ffrtmphttp              libzmq                  tcp
file                    md5                     tee
ftp                     mmsh                    tls
gopher                  mmst                    udp
gophers                 pipe                    udplite
hls                     prompeg

Enabled filters:
a3dscope                deband                  pan
aap                     deblock                 perlin
abench                  decimate                perms
abitscope               deconvolve              perspective
acompressor             dedot                   phase
acontrast               deesser                 photosensitivity
acopy                   deflate                 pixdesctest
acrossfade              deflicker               pixelize
acrossover              deinterlace_qsv         pixscope
acrusher                deinterlace_vaapi       pp
acue                    dejudder                pp7
addroi                  delogo                  premultiply
adeclick                denoise_vaapi           prewitt
adeclip                 deshake                 prewitt_opencl
adecorrelate            deshake_opencl          procamp_vaapi
adelay                  despill                 program_opencl
adenorm                 detelecine              pseudocolor
aderivative             dialoguenhance          psnr
adrawgraph              dilation                pullup
adrc                    dilation_opencl         qp
adynamicequalizer       displace                qrencode
adynamicsmooth          doubleweave             qrencodesrc
aecho                   drawbox                 quirc
aemphasis               drawbox_vaapi           random
aeval                   drawgraph               readeia608
aevalsrc                drawgrid                readvitc
aexciter                drawtext                realtime
afade                   drmeter                 remap
afdelaysrc              dynaudnorm              remap_opencl
afftdn                  earwax                  removegrain
afftfilt                ebur128                 removelogo
afir                    edgedetect              repeatfields
afireqsrc               elbg                    replaygain
afirsrc                 entropy                 reverse
aformat                 epx                     rgbashift
afreqshift              eq                      rgbtestsrc
afwtdn                  equalizer               roberts
agate                   erosion                 roberts_opencl
agraphmonitor           erosion_opencl          rotate
ahistogram              estdif                  rubberband
aiir                    exposure                sab
aintegral               extractplanes           scale
ainterleave             extrastereo             scale2ref
alatency                fade                    scale_cuda
alimiter                feedback                scale_qsv
allpass                 fftdnoiz                scale_vaapi
allrgb                  fftfilt                 scale_vulkan
allyuv                  field                   scdet
aloop                   fieldhint               scharr
alphaextract            fieldmatch              scroll
alphamerge              fieldorder              segment
amerge                  fillborders             select
ametadata               find_rect               selectivecolor
amix                    firequalizer            sendcmd
amovie                  flanger                 separatefields
amplify                 flip_vulkan             setdar
amultiply               flite                   setfield
anequalizer             floodfill               setparams
anlmdn                  format                  setpts
anlmf                   fps                     setrange
anlms                   framepack               setsar
anoisesrc               framerate               settb
anull                   framestep               sharpness_vaapi
anullsink               freezedetect            shear
anullsrc                freezeframes            showcqt
apad                    frei0r                  showcwt
aperms                  frei0r_src              showfreqs
aphasemeter             fspp                    showinfo
aphaser                 fsync                   showpalette
aphaseshift             gblur                   showspatial
apsnr                   gblur_vulkan            showspectrum
apsyclip                geq                     showspectrumpic
apulsator               gradfun                 showvolume
arealtime               gradients               showwaves
aresample               graphmonitor            showwavespic
areverse                grayworld               shuffleframes
arls                    greyedge                shufflepixels
arnndn                  guided                  shuffleplanes
asdr                    haas                    sidechaincompress
asegment                haldclut                sidechaingate
aselect                 haldclutsrc             sidedata
asendcmd                hdcd                    sierpinski
asetnsamples            headphone               signalstats
asetpts                 hflip                   signature
asetrate                hflip_vulkan            silencedetect
asettb                  highpass                silenceremove
ashowinfo               highshelf               sinc
asidedata               hilbert                 sine
asisdr                  histeq                  siti
asoftclip               histogram               smartblur
aspectralstats          hqdn3d                  smptebars
asplit                  hqx                     smptehdbars
ass                     hstack                  sobel
astats                  hstack_qsv              sobel_opencl
astreamselect           hstack_vaapi            sofalizer
asubboost               hsvhold                 spectrumsynth
asubcut                 hsvkey                  speechnorm
asupercut               hue                     split
asuperpass              huesaturation           spp
asuperstop              hwdownload              ssim
atadenoise              hwmap                   ssim360
atempo                  hwupload                stereo3d
atilt                   hwupload_cuda           stereotools
atrim                   hysteresis              stereowiden
avectorscope            iccdetect               streamselect
avgblur                 iccgen                  subtitles
avgblur_opencl          identity                super2xsai
avgblur_vulkan          idet                    superequalizer
avsynctest              il                      surround
axcorrelate             inflate                 swaprect
azmq                    interlace               swapuv
backgroundkey           interleave              tblend
bandpass                join                    telecine
bandreject              kerndeint               testsrc
bass                    kirsch                  testsrc2
bbox                    ladspa                  thistogram
bench                   lagfun                  threshold
bilateral               latency                 thumbnail
bilateral_cuda          lenscorrection          thumbnail_cuda
biquad                  lensfun                 tile
bitplanenoise           libplacebo              tiltandshift
blackdetect             libvmaf                 tiltshelf
blackframe              life                    tinterlace
blend                   limitdiff               tlut2
blend_vulkan            limiter                 tmedian
blockdetect             loop                    tmidequalizer
blurdetect              loudnorm                tmix
bm3d                    lowpass                 tonemap
boxblur                 lowshelf                tonemap_opencl
boxblur_opencl          lumakey                 tonemap_vaapi
bs2b                    lut                     tpad
bwdif                   lut1d                   transpose
bwdif_cuda              lut2                    transpose_opencl
bwdif_vulkan            lut3d                   transpose_vaapi
cas                     lutrgb                  transpose_vulkan
ccrepack                lutyuv                  treble
cellauto                mandelbrot              tremolo
channelmap              maskedclamp             trim
channelsplit            maskedmax               unpremultiply
chorus                  maskedmerge             unsharp
chromaber_vulkan        maskedmin               unsharp_opencl
chromahold              maskedthreshold         untile
chromakey               maskfun                 uspp
chromakey_cuda          mcdeint                 v360
chromanr                mcompand                vaguedenoiser
chromashift             median                  varblur
ciescope                mergeplanes             vectorscope
codecview               mestimate               vflip
color                   metadata                vflip_vulkan
color_vulkan            midequalizer            vfrdet
colorbalance            minterpolate            vibrance
colorchannelmixer       mix                     vibrato
colorchart              monochrome              vidstabdetect
colorcontrast           morpho                  vidstabtransform
colorcorrect            movie                   vif
colorhold               mpdecimate              vignette
colorize                mptestsrc               virtualbass
colorkey                msad                    vmafmotion
colorkey_opencl         multiply                volume
colorlevels             negate                  volumedetect
colormap                nlmeans                 vpp_qsv
colormatrix             nlmeans_opencl          vstack
colorspace              nlmeans_vulkan          vstack_qsv
colorspace_cuda         nnedi                   vstack_vaapi
colorspectrum           noformat                w3fdif
colortemperature        noise                   waveform
compand                 normalize               weave
compensationdelay       null                    xbr
concat                  nullsink                xcorrelate
convolution             nullsrc                 xfade
convolution_opencl      openclsrc               xfade_opencl
convolve                oscilloscope            xfade_vulkan
copy                    overlay                 xmedian
corr                    overlay_cuda            xpsnr
cover_rect              overlay_opencl          xstack
crop                    overlay_qsv             xstack_qsv
cropdetect              overlay_vaapi           xstack_vaapi
crossfeed               overlay_vulkan          yadif
crystalizer             owdenoise               yadif_cuda
cue                     pad                     yaepblur
curves                  pad_opencl              yuvtestsrc
datascope               pad_vaapi               zmq
dblur                   pal100bars              zoneplate
dcshift                 pal75bars               zoompan
dctdnoiz                palettegen              zscale
ddagrab                 paletteuse

Enabled bsfs:
aac_adtstoasc           h264_mp4toannexb        pcm_rechunk
av1_frame_merge         h264_redundant_pps      pgs_frame_merge
av1_frame_split         hapqa_extract           prores_metadata
av1_metadata            hevc_metadata           remove_extradata
chomp                   hevc_mp4toannexb        setts
dca_core                imx_dump_header         showinfo
dovi_rpu                media100_to_mjpegb      text2movsub
dts2pts                 mjpeg2jpeg              trace_headers
dump_extradata          mjpega_dump_header      truehd_core
dv_error_marker         mov2textsub             vp9_metadata
eac3_core               mpeg2_metadata          vp9_raw_reorder
evc_frame_merge         mpeg4_unpack_bframes    vp9_superframe
extract_extradata       noise                   vp9_superframe_split
filter_units            null                    vvc_metadata
h264_metadata           opus_metadata           vvc_mp4toannexb

Enabled indevs:
dshow                   lavfi                   vfwcap
gdigrab                 libcdio

Enabled outdevs:
caca                    sdl2

git-full external libraries' versions: 

AMF v1.4.35-3-g8f5a645
aom v3.11.0-160-g433be28b4f
aribb24 v1.0.3-5-g5e9be27
aribcaption 1.1.1
AviSynthPlus v3.7.3-93-g8ef2e32d
bs2b 3.1.0
chromaprint 1.5.1
codec2 1.2.0-103-gff00a6e2
dav1d 1.5.0-51-g5ea4939
davs2 1.7-1-gb41cf11
ffnvcodec n12.2.72.0-1-g9934f17
flite v2.2-55-g6c9f20d
freetype VER-2-13-3
frei0r v2.3.3-7-g9178c72
fribidi v1.0.16-1-gcfc71cd
gsm 1.0.22
harfbuzz 10.1.0-38-gb5a65e0f
ladspa-sdk 1.17
lame 3.100
lc3 1.1.0
lcms2 2.16
lensfun v0.3.95-1608-gbd8ee173
libass 0.17.3-61-g95e33ec
libcdio-paranoia 10.2
libgme 0.6.3
libilbc v3.0.4-346-g6adb26d4a4
libopencore-amrnb 0.1.6
libopencore-amrwb 0.1.6
libplacebo v7.349.0-30-g056b852
libsoxr 0.1.3
libssh 0.11.1
libtheora 1.1.1
libwebp v1.5.0-1-g2af6c034
oneVPL 2.14
OpenCL-Headers v2024.10.24
openmpt libopenmpt-0.6.21-20-g61a36420c
opus v1.5.2-22-g7db26934
qrencode 4.1.1
quirc 1.2
rav1e p20241015-4-g62b4888
rist 0.2.12
rubberband v1.8.1
SDL prerelease-2.29.2-460-gfc608ffb5
shaderc v2024.4-5-g690d259
shine 3.1.1
snappy 1.2.1
speex Speex-1.2.1-32-g440f3ea
srt v1.5.4-12-g8a89a3a
SVT-AV1 v2.3.0-100-g783c3f1f
twolame 0.4.0
uavs3d v1.1-47-g1fd0491
VAAPI 2.23.0.
vidstab v1.1.1-13-g8dff7ad
vmaf v3.0.0-99-g8cde19dc
vo-amrwbenc 0.1.3
vorbis v1.3.7-10-g84c02369
vpx v1.15.0-35-g8058a0b54
vulkan-loader v1.4.304-4-g4c1027d
vvenc v1.13.0-3-g81a3b6c
x264 v0.164.3199
x265 4.1-54-gfa2770934
xavs2 1.4
xevd 0.5.0
xeve 0.5.1
xvid v1.3.7
zeromq 4.3.5
zimg release-3.0.5-173-g30f368c
zvbi v0.2.43-2-g7a76c67

